#!/bin/bash
echo server setup

servers=(
    megamedes.cs.rice.edu
    styx.cs.rice.edu
    oceanus.cs.rice.edu
    tethys.cs.rice.edu
)

localFolder=(
    megamedes
    styx
    oceanus
    tethys
)

make_dir(){
    for i in "${localFolder[@]}"
    do
        $1 $2 $i
    done
}

#make_dir rm -rf
make_dir mkdir -p
j=0
for i in "${servers[@]}"
    do
        scp -r ar103@$i:/home/ar103/redwan/T_ASE_SERVER/OUT ./${localFolder[j++]}
    done

#scp -r ar103:$i:/home/ar103/redwan/T_ASE_SERVER/output/
#scp -r username@server_ip:/path_to_remote_directory local-machine/path_to_the_directory/
