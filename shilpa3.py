import requests
import smtplib
from email.message import EmailMessage

def vegetable_store():
    try:
        url = "http://demo3278802.mockable.io/Vegetable_Store_Data"  # Example API URL
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            vegetable_name = data.get("VegetableName", "Unknown")
            price = data.get("Price", 0)

            quantity = int(input(f"Enter quantity of {vegetable_name} (kg): "))
            total_price = price * quantity
            gst = (total_price * 5) / 100  # 5% GST
            final_bill = total_price + gst

            print("\n--- BILL DETAILS ---")
            print(f"Item: {vegetable_name}")
            print(f"Price per kg: {price}")
            print(f"Quantity: {quantity} kg")
            print(f"Total price: {total_price}")
            print(f"GST (5%): {gst}")
            print(f"Final Amount: {final_bill}")
            print("--------------------\n")

            bill_method = int(input("Press 1 for email bill, 2 for printed bill: "))

            if bill_method == 1:
                send_email_bill(vegetable_name, total_price, gst, final_bill)
            elif bill_method == 2:
                save_printed_bill(vegetable_name, total_price, gst, final_bill)
            else:
                print("Invalid input. Please choose 1 or 2.")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")

def send_email_bill(vegetable, total, gst, final):
    try:
        sender_email = "your_email@gmail.com"
        receiver_email = "customer_email@gmail.com"
        password = "your_password"

        msg = EmailMessage()
        msg["Subject"] = "Your Vegetable Store Bill"
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg.set_content(f"""
        Your Bill:
        Item: {vegetable}
        Total Price: {total}
        GST (5%): {gst}
        Final Amount: {final}
        """)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.send_message(msg)
        
        print("Email bill sent successfully!")

    except Exception as e:
        print(f"Error sending email: {e}")

def save_printed_bill(vegetable, total, gst, final):
    try:
        with open("vegetable_bill.txt", "w") as file:
            file.write(f"""
            --- BILL RECEIPT ---
            Item: {vegetable}
            Total Price: {total}
            GST (5%): {gst}
            Final Amount: {final}
            --------------------
            """)
        print("Bill saved as 'vegetable_bill.txt'. You can print it.")
    
    except Exception as e:
        print(f"Error saving bill: {e}")

vegetable_store()