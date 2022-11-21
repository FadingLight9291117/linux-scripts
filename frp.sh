# !/bin/bash

frp_dir=/home/clz/local/frp

if [ -e $frpc_dir  ]
then
    $frp_dir/frpc -c $frp_dir/frpc.ini
fi
