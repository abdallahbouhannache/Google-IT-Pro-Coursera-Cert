#!/bin/bash


. ./library.lib

# dataset[name]=name
# dataset[phone]=31154689432
# dataset[age]=45
# dataset[email]=me@gmail.com

greeting()
{
  line=--
  echo " "
  echo "$line please select one of the three choices: $line"
  echo "Search for address book : 1"
  echo "Add / Remove :2"
  echo "edit entries :3"
  echo "Quit ! :4"
  echo "$line "
}

dataread
exit

while :
do
  greeting
  read choice
  case $choice in
	1)
    echo "main Searching for someone,please type Name or Surname or Email or Phone!";
      dataread
    echo " mainsearching for :${dataset[@]}"
    dataset ;;
	2)
		read -p "1 for Add and 2 to Remove an contact !" ch;
      dataread
      if [ $ch -eq "1" ];then
          echo "main Creating new contact"
          addnewcontact 
      else 
          echo "main deleting"
          delnewcontact
      fi
		;;
	3)
    while :
    do
      echo  "Write contact you wanna Edit !";
      dataread
      echo "------------------------"
      echo "------${dataset[@]}-----"
      echo "------------------------"
      read -p "Is this the contact you want to change [Yn]!" ans;
      if [ $ans = 'y' ] || [ $ans = "Y" ];then
        modifycontact dataset
        break
      fi
    done
		;;
    4)
      echo "Thanks for using our addressbook,bye ...!"
        exit
		;;
    *)
		  echo "Try again please select a choice among 1-3 "
		;;
  esac
done

##Name, Surname, Email, Phone, etc