import tkinter as tk
from tkinter import ttk, messagebox

# เมนูและราคา
menu_items = {
    "Tuna Tartare Salsa": 125,
    "Cordon Bleu Chicken": 145,
    "Salmon Steak with Sauce": 169,
    "Caesar Salad": 139,
    "Sparkling Sunset": 90,
    "Coke Mojito": 60,
}

# รายการคำสั่งซื้อ
order_list = []

# ฟังก์ชันสำหรับเพิ่มรายการ
def add_to_order():
    selected_item = menu_combobox.get()
    try:
        qty = int(quantity_entry.get())
        if qty <= 0:
            raise ValueError
        price = menu_items[selected_item] * qty
        order_list.append({"item": selected_item, "qty": qty, "price": price})
        update_order_table()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid quantity.")

# ฟังก์ชันสำหรับอัปเดตรายการในตาราง
def update_order_table():
    for row in order_table.get_children():
        order_table.delete(row)
    for idx, order in enumerate(order_list, start=1):
        order_table.insert("", "end", values=(idx, order['item'], order['qty'], order['price']))

# ฟังก์ชันคำนวณราคาสุทธิ
def calculate_total():
    if not order_list:
        messagebox.showerror("No Orders", "Please add items to the order before calculating.")
        return
    
    total_price = sum(order['price'] for order in order_list)
    discount = 0
    if member_var.get():
        discount = total_price * 0.10
    price_after_discount = total_price - discount
    vat = price_after_discount * 0.07
    grand_total = price_after_discount + vat

    # แสดงผลในข้อความ
    total_label.config(text=f"Total: {total_price:.2f} THB")
    discount_label.config(text=f"Discount: {discount:.2f} THB")
    vat_label.config(text=f"VAT (7%): {vat:.2f} THB")
    grand_total_label.config(text=f"Grand Total: {grand_total:.2f} THB")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Food Order System")
root.geometry("700x500")
root.configure(bg="#f0f0f0")

# ส่วนหัว
header_label = tk.Label(root, text="Food Order System", font=("Helvetica", 20, "bold"), bg="#f0f0f0")
header_label.pack(pady=10)

# แสดงเมนูอาหาร
frame_top = tk.Frame(root, bg="#f0f0f0")
frame_top.pack(pady=10)

menu_label = tk.Label(frame_top, text="Select Menu:", font=("Helvetica", 12), bg="#f0f0f0")
menu_label.grid(row=0, column=0, padx=10, pady=10)

menu_combobox = ttk.Combobox(frame_top, values=list(menu_items.keys()), state="readonly", width=30)
menu_combobox.grid(row=0, column=1, padx=10, pady=10)
menu_combobox.current(0)

quantity_label = tk.Label(frame_top, text="Quantity:", font=("Helvetica", 12), bg="#f0f0f0")
quantity_label.grid(row=1, column=0, padx=10, pady=10)

quantity_entry = tk.Entry(frame_top, font=("Helvetica", 12), width=10)
quantity_entry.grid(row=1, column=1, padx=10, pady=10)

add_button = tk.Button(frame_top, text="Add to Order", font=("Helvetica", 12), command=add_to_order, bg="#007BFF", fg="white")
add_button.grid(row=2, column=0, columnspan=2, pady=10)

# ตารางแสดงรายการอาหาร
frame_middle = tk.Frame(root, bg="#f0f0f0")
frame_middle.pack(pady=10)

order_table = ttk.Treeview(frame_middle, columns=("No", "Item", "Quantity", "Price"), show="headings", height=10)
order_table.heading("No", text="No")
order_table.heading("Item", text="Item")
order_table.heading("Quantity", text="Quantity")
order_table.heading("Price", text="Price (THB)")

order_table.column("No", width=50, anchor="center")
order_table.column("Item", width=200, anchor="w")
order_table.column("Quantity", width=100, anchor="center")
order_table.column("Price", width=100, anchor="e")
order_table.pack()

# ตัวเลือกสมาชิก BU Card
member_var = tk.BooleanVar()
member_checkbox = tk.Checkbutton(root, text="BU Member Card (10% Discount)", variable=member_var, font=("Helvetica", 12), bg="#f0f0f0")
member_checkbox.pack(pady=10)

# ปุ่มคำนวณ
calculate_button = tk.Button(root, text="Calculate Total", font=("Helvetica", 14, "bold"), command=calculate_total, bg="#28A745", fg="white")
calculate_button.pack(pady=10)

# แสดงผลรวม
frame_bottom = tk.Frame(root, bg="#f0f0f0")
frame_bottom.pack(pady=10)

total_label = tk.Label(frame_bottom, text="Total: 0.00 THB", font=("Helvetica", 12), bg="#f0f0f0")
total_label.grid(row=0, column=0, padx=10, pady=5)

discount_label = tk.Label(frame_bottom, text="Discount: 0.00 THB", font=("Helvetica", 12), bg="#f0f0f0")
discount_label.grid(row=1, column=0, padx=10, pady=5)

vat_label = tk.Label(frame_bottom, text="VAT (7%): 0.00 THB", font=("Helvetica", 12), bg="#f0f0f0")
vat_label.grid(row=2, column=0, padx=10, pady=5)

grand_total_label = tk.Label(frame_bottom, text="Grand Total: 0.00 THB", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
grand_total_label.grid(row=3, column=0, padx=10, pady=5)

# เริ่มโปรแกรม
root.mainloop()
