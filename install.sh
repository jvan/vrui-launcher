#!/bin/bash
#
# Install script for VruiLauncher program.
#

source root-check.sh
source term-colors.sh

ROOTDIR=`dirname $0`

INSTALLDIR=/usr/local
SHAREDIR=$INSTALLDIR/share/vrui-launcher

if [[ ! -e "$SHAREDIR" ]]; then
   echo $(status WARN "creating directory $SHAREDIR")
   mkdir -p $SHAREDIR
fi

echo $(status MSG "installing gsettings schema")
pushd $PWD 1>/dev/null
cd $ROOTDIR/etc
./install_schema
popd 1>/dev/null

echo $(status MSG "copying fragments to $SHAREDIR/fragments")
cp -r $ROOTDIR/fragments $SHAREDIR/fragments

echo $(status MSG "copying templates to $SHAREDIR/templates")
cp -r $ROOTDIR/templates $SHAREDIR/templates

MODULE=$ROOTDIR/vruilauncher

echo $(status MSG "installing python module")
cp -r $ROOTDIR/vruilauncher $INSTALLDIR/lib/python2.7/dist-packages

echo $(status MSG "installing binaries")
cp vrui-launcher $INSTALLDIR/bin
cp vrui_launcher_settings.py $INSTALLDIR/bin

