from django.contrib import admin
from .models import OAuthSettings
from django.contrib import admin
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from .models import Invitation

@admin.register(OAuthSettings)
class OAuthSettingsAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'redirect_uri', 'created_at')


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('email', 'invited_at', 'is_used')  # Removed 'token'
    actions = ['send_invitation_email']

    def send_invitation_email(self, request, queryset):
        for invitation in queryset:
            try:
                # Generate the registration link (without token)
                registration_link = request.build_absolute_uri(
                    reverse('register')  # Direct link to the register page
                )

                # Define the HTML content for the email
                email_subject = 'You are Invited!'
                email_body = f"""
                <html>
                  <head>
                    <style>
                      body {{
                        font-family: Arial, sans-serif;
                        background-color: #f7f7f7;
                        margin: 0;
                        padding: 0;
                      }}
                      .email-container {{
                        width: 100%;
                        max-width: 600px;
                        margin: 20px auto;
                        background-color: #ffffff;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                      }}
                      .email-header {{
                        text-align: center;
                        padding-bottom: 20px;
                      }}
                      .email-header h1 {{
                        font-size: 24px;
                        color: #333333;
                      }}
                      .email-content {{
                        font-size: 16px;
                        color: #555555;
                        line-height: 1.5;
                      }}
                      .button {{
                        display: inline-block;
                        margin-top: 20px;
                        padding: 12px 24px;
                        background-color: #007BFF;
                        color: #ffffff;
                        font-size: 16px;
                        text-decoration: none;
                        border-radius: 5px;
                        text-align: center;
                      }}
                      .footer {{
                        text-align: center;
                        margin-top: 40px;
                        font-size: 14px;
                        color: #999999;
                      }}
                    </style>
                  </head>
                  <body>
                    <div class="email-container">
                      <div class="email-header">
                        <h1>You're Invited to Join Task Manager App!</h1>
                      </div>
                      <div class="email-content">
                        <p>Hi there!</p>
                        <p>We are excited to invite you to join the Task Manager App. Please click the link below to complete your registration:</p>
                        <a href="{registration_link}" class="button">Register Now</a>
                        <p>If the button above doesn't work, you can copy and paste the following link into your browser:</p>
                        <p><a href="{registration_link}">{registration_link}</a></p>
                      </div>
                      <div class="footer">
                        <p>Thank you for using Task Manager App!</p>
                        <p>If you have any questions, feel free to contact us.</p>
                      </div>
                    </div>
                  </body>
                </html>
                """

                # Send the invitation email with HTML content
                send_mail(
                    email_subject,
                    '',
                    settings.DEFAULT_FROM_EMAIL,  # From email address
                    [invitation.email],  # Recipient's email address
                    html_message=email_body,  # Pass the HTML content
                    fail_silently=False
                )
                self.message_user(request, f'Invitation sent to {invitation.email}')
            except Exception as e:
                self.message_user(request, f'Error sending invitation to {invitation.email}: {str(e)}', level=messages.ERROR)

    send_invitation_email.short_description = "Send Registration Invitation Email"
