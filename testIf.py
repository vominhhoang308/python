guess_count = 0
correct_pass = "minhhoang308"

while True:
    if guess_count < 3:
        guess_pass = raw_input("What is your password: ")
        if guess_pass == correct_pass:
            print "Your password is correct"
            break
        else:
            print "Your password is not correct. Try again"
            guess_count += 1
    else:
        print "You have been denied access"
        break
    


