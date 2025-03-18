# DMOJ problem ecoo13r1p1, Take a Number
# next_number = int(input())
# queue = []
# late_students = 0
# 
# while True:
#     command = input().strip()
#         
#     if command == 'EOF':
#         break
#     
#     if command == 'TAKE':
#         queue.append(next_number)
#         late_students += 1
#         next_number = next_number + 1 if next_number < 999 else 1
#                 
#     elif command == 'SERVE':
#         if queue:
#             queue.pop(0)
#             late_students -= 1
#             
#     elif command == 'CLOSE':
#         print(late_students, len(queue), next_number)
#         late_students = 0

from collections import deque

def main():
    # Read the initial next number
    next_number = int(input())
    queue = deque()  # Queue to store waiting students
    late_students = 0  # Counter for late students

    while True:
        command = input().strip()  # Read the next command
        if command == "EOF":
            break  # End of input

        if command == "TAKE":
            # Add the next number to the queue
            queue.append(next_number)
            late_students += 1
            # Increment next_number, reset to 1 if it exceeds 999
            next_number = next_number + 1 if next_number < 999 else 1

        elif command == "SERVE":
            # Serve the next student in the queue
            if queue:
                queue.popleft()
                late_students -= 1  # Decrement the counter

        elif command == "CLOSE":
            # Print the required statistics
            print(late_students, len(queue), next_number)
            # Reset late_students for the next day
            late_students = 0

if __name__ == "__main__":
    main()
