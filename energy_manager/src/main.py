import asyncio
from energy_manager import (
    cost_of_power_consumption,
    append_to_json,
    calculate_total_cost_from_json,
    get_float_input,
    ask_kernel,
    ask_kernel_with_data,
)

def main():
    cost = None
    consumption_per_hour = None

    while True:
        print("\n===== Energy Manager Menu =====")
        print("1. Show consumption per second")
        print("2. Show consumption per hour")
        print("3. Show consumption per month")
        print("4. Calculate total cost of all devices")
        print("5. Get AI-generated feedback on consumption")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            device = input("Enter device name: ")
            number_of_device = input("Enter number of this device: ")
            power_rating_watts = get_float_input("Enter power rating of device in watts (W): ")
            currency = input("Enter your currency: ")
            cost_per_kwh = get_float_input("Enter electricity cost per kWh: ")

            # Calculate cost per second
            cost = cost_of_power_consumption(power_rating_watts, cost_per_kwh)
            if cost:
                print(f"Using {device} costs {currency} {cost:.10f} per second.")

                # Append data
                append_to_json({
                    "device": device,
                    "number_of_device": number_of_device,
                    "power_rating": power_rating_watts,
                    "currency": currency,
                    "cost": cost,
                })

        elif choice == '2':
            if cost:
                consumption_per_hour = cost * 3600
                print(f"Total consumption per hour: {consumption_per_hour}")
            else:
                print("⚠️ Calculate per second cost first.")

        elif choice == '3':
            if consumption_per_hour:
                consumption_hours_per_day = get_float_input("Enter how many hours device is used daily: ")
                consumption_per_month = consumption_per_hour * consumption_hours_per_day * 30
                print(f"Total consumption per month: {consumption_per_month}")
            else:
                print("⚠️ Calculate hourly consumption first.")

        elif choice == '4':
            total_cost = calculate_total_cost_from_json()
            print(f"Total consumption of all saved devices: {total_cost}")

        elif choice == '5':
            question = input("Ask your question: ")
            answer = asyncio.run(ask_kernel(question))
            insight = asyncio.run(ask_kernel_with_data(question))
            print(f"As your trusted Energy Management Consultant: {answer, insight}")

        elif choice == '0':
            print("Exiting Energy Manager. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()