<<<<<<< HEAD
#!/usr/bin/python3
=======
 #!/usr/bin/python3
>>>>>>> 5e49c5a8601cd050c51168b16df85a6fea6a710c
def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            count += 1

    print()
    return (count)
