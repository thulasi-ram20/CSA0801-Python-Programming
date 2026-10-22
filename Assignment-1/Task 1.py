

BASE_RATE = 30.00
BASE_FAT = 3.5
BASE_SNF = 8.5
FAT_ADJUSTMENT = 0.40
SNF_ADJUSTMENT = 0.30

farmer_id = input("Enter farmer ID: ")
litres = float(input("Enter milk quantity in litres: "))
fat = float(input("Enter fat percentage: "))
snf = float(input("Enter SNF percentage: "))
shift = input("Enter shift (Morning/Evening): ").strip().title()

# Validate inputs
if litres < 0:
    print("Error: Milk quantity cannot be negative.")
elif not 2.0 <= fat <= 7.0:
    print("Error: Fat must be between 2% and 7%.")
elif snf < 0:
    print("Error: SNF cannot be negative.")
elif shift not in ("Morning", "Evening"):
    print("Error: Invalid shift.")
else:
    # Calculate rate per litre
    fat_difference = (fat - BASE_FAT) / 0.1
    snf_difference = (snf - BASE_SNF) / 0.1

    rate = (BASE_RATE
            + fat_difference * FAT_ADJUSTMENT
            + snf_difference * SNF_ADJUSTMENT)

    # Prevent negative payment rates
    if rate < 0:
        print("Error: Calculated rate cannot be negative.")
    else:
        payment = litres * rate

        # Assumption: same payment for 10 days
        ten_day_total = payment * 10

        print("\n--- Milk Payment Details ---")
        print("Farmer ID:", farmer_id)
        print("Shift:", shift)
        print("Rate per litre: Rs.", round(rate, 2))
        print("Payment amount: Rs.", round(payment, 2))
        print("Ten-day total: Rs.", round(ten_day_total, 2))
