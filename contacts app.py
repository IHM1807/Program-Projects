#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 19:33:42 2023

@author: yusufhagimohamed
"""

def view_contacts(contacts):
    print(contacts)

def add_contacts(contacts, name, number):
    contacts.append((name, number))
    print(name, number, "has been added to contacts")
    
def delete_contacts(contacts, name, number):
    contacts.remove((name, number))
    print("Deleting", name, number,)

def quit_choice():
    print("Goodbye")

def main(contacts=["Ismaill,                627"               ,                    "Yusuf,             423"]):
    while True:
        print("\nPlease choose from the following:")
        print("v - View contacts")
        print("a - Add contacts")
        print("d - Delete contacts")
        print("q - Quit")

        choice = input("\nEnter a choice (v, a, d, q)")

        if choice == "v":
            print("\n---- View contacts ----")
            view_contacts( contacts)
        elif choice == "a":
            print("\n--------- Add contacts -----------")
            name = input("\nPlease enter your name: ")
            number = input("\nPlease enter your number: ")
            add_contacts(contacts, name, number)
        elif choice == "d":
            print("\n-------- Delete contacts ---------")
            name = input("\nEnter the contact name you wish to delete: ")
            number = input("\nEnter the contact number you wish to delete: ")
            delete_contacts(contacts, name, number)
        elif choice == "q":
            print("\n-------Goodbye--------")
            break
        else:
            print("You have entered an invalid choice. Try again")

if __name__ == "__main__":
    main()