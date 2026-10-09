distances = [3.0, 4.5, 0.0, 6.0]
#distances = []
if len(distances) == 0:
    print("No sessions logged.")
else: 
    sessions = len(distances)
    total = sum(distances)
    longest = max(distances)
    average = total/sessions

    print("Logged sessions:", sessions)
    print(f"Total mileage: {total:.2f} miles")

    print(f"Longest run: {longest:.2f} miles")
    print(f"Average distance: {average:.2f} miles")