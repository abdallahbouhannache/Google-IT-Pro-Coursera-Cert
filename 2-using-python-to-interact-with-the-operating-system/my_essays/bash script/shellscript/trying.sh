#!/bin/bash



# declare -A dataset
# database=()
# dataset[name]=name
# dataset[phone]=31154689432
# dataset[age]=45
# dataset[email]=me@gmail.com
# echo dataset
# #echo ${dataset[@]}
# echo ${database[@]}
# database+=(dataset)
# echo ${database[@]}


# for key in "${!database[@]}"; do
#     echo "$key ${database[$key]}"
# done

funcm()
{
    read -p "[name] :" name;
    return "ddd"
}

function F2()
{
    local  retval='Using BASH Function'
    
}

getval=$(F2)  
echo $getval