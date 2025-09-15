from django.conf import settings
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
account_activation_token = PasswordResetTokenGenerator()

def email_func(user):
    token = account_activation_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    absurl = f"{settings.FRONTEND_URL}/reset-password/{uid}/{token}/"
    name = f"{user.name} - {user.employee_id}"
    logo_url = r"https://pub-082bdb23d3f64d9ba2fee9181e5fe388.r2.dev/media/gmb-2025-08-28T07-07-58.png"

    email_body = f""" <body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f6f9;" >
                        <div style="max-width: 520px; margin: 40px auto; background-color: #fff; overflow: hidden; 
                            border-radius: 12px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.8); ">
                                
                          <!-- Logo -->
                          <div style="text-align: center; padding: 10px; background: #f15a23"> <img src="{logo_url}" 
                          alt="Logo" style="max-width: 190px"/></div>
                
                          <!-- Content -->
                          <div style="text-align: center; padding: 30px 25px">
                            <h2 style="color: #222; margin-bottom: 10px">Dear {name},</h2>
                            
                            <p style="color: #555; font-size: 15px; line-height: 1.6; margin: 0 auto 25px; max-width: 420px;">
                              We received a request to reset your password. To continue, please click the button below.</p>
                
                            <!-- Button -->
                            <div style="margin: 25px 0"><a href="{absurl}"
                                style="display: inline-block; background-color: #007bff; color: #fff; 
                                padding: 14px 32px; text-decoration: none; border-radius: 8px; font-size: 16px; 
                                font-weight: bold; margin-top: 15px;
                                "onmouseover="this.style.backgroundColor='#0056b3'
                                "onmouseout="this.style.backgroundColor='#007bff'">Reset Password</a>
                            </div>
                            
                            <p style="color: #999; font-size: 13px; margin-top: 25px; line-height: 1.5;">
                              No worries if you didn’t request this — simply ignore this email.<br /></p>
                              
                            <!-- Footer -->
                            <div style="background-color: #f8f9fa; padding: 15px; text-align: center; border-top: 1px solid #eee;">
                              <p style="color: #777; font-size: 13px; margin: 0"> Regards, 
                              <br /><strong>Poorvika Mobiles Pvt Ltd</strong></p></div>
                          </div>
                        </div>
                      </body>"""

    plain_message = (f"{logo_url},\n\nHello {name},\n\n" 
                     f"You requested a password reset. Please click the link below:\n" 
                     f"{absurl}\n\nIf you did not request this, please ignore.")

    return email_body, plain_message
