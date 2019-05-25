#!/usr/bin/env bash

servers=(
    megamedes.cs.rice.edu
    styx.cs.rice.edu
    oceanus.cs.rice.edu
    tethys.cs.rice.edu
)

SERVER_NAME="styx.cs.rice.edu"
scp -r ar103@$SERVER_NAME:/home/ar103/redwan/T_ASE_SERVER_PREBUILD/OUT ./output/

