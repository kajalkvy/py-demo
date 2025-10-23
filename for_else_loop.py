# for number in range(1,3):
#     print(number, "Attempt")
#     score = input("score : ")
#     if bool(score):
#         print("Successful")
#         break
#     else:
#         print("Failed")
for number in range(1,3):
    print(number, "Attempt")
    score = input("score : ")
    if int(score)>=60:
        print("Successful")
        break
    else:
        print("Failed")