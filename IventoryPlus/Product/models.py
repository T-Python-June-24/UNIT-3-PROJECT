from datetime import date
from django.db import models
from Supplier.models import Supplier
from Category.models import Category
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os


class Product(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    suppliers = models.ManyToManyField(Supplier)
    expiry_date = models.DateField()
    stock = models.IntegerField(default=0)  # Current inventory level
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    minimum_stock = models.IntegerField(default=0)  # Minimum required stock level
    

    def send_email(self, subject, message, html_content):
        sender_email = "sarahmoniftest@gmail.com"
        receiver_email = "sarahmoniftest@gmail.com"
        
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        part1 = MIMEText("Stock Status Notification", 'plain')
        part2 = MIMEText(html_content, 'html')
        msg.attach(part1)
        msg.attach(part2)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        load_dotenv()
        EMAIL_KEY=os.getenv("EMAIL_KEY")
        server.login(sender_email, EMAIL_KEY)  # Secure your credentials
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

    def stock_status(self):
        subject = f"Stock Status of {self.name}"

        if self.stock <= 0:
            message = f"{self.name} is Out of Stock"
            html_content = f"""\
            <html>
            <head></head>
            <body>
                <p>Hi,<br>
                   <b>Stock Status:</b> {message}<br>
                   The inventory is depleted. Immediate attention required!
                </p>
            </body>
            </html>
            """
            self.send_email(subject, message, html_content)
            return 'Out of Stock'
        elif self.stock <= self.minimum_stock:
            message = f"{self.name} is in Low Stock"
            html_content = f"""\
            <html>
            <head></head>
            <body>
                <p>Hi,<br>
                   <b>Stock Status:</b> {message}<br>
                   Please check the inventory, as the stock is low.
                </p>
            </body>
            </html>
            """
            self.send_email(subject, message, html_content)
            return 'Low Stock'
        else:
            return 'In Stock'



    def __str__(self):
        return self.name
    
   