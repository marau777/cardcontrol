#!/bin/bash
CARDCONTROL_SRC_DIR="$(pwd)/src"
CARDCONTROL_INSTALL_DIR="/usr/local/bin"
CARDCONTROL_SERVICES_DIR="/etc/systemd/system"
CARDCONTROL_WEBSERVER_SERVICE="cardcontrol-webservice.service"
CARDCONTROL_DISPLAYSTATS_SERVICE="cardcontrol-display-stats.service"

cp $CARDCONTROL_SRC_DIR/*.py $CARDCONTROL_INSTALL_DIR
cp $CARDCONTROL_SRC_DIR/*.js $CARDCONTROL_INSTALL_DIR
cp -rf $CARDCONTROL_SRC_DIR/node_modules $CARDCONTROL_INSTALL_DIR
cp $CARDCONTROL_SRC_DIR/*.html $CARDCONTROL_INSTALL_DIR
cp $CARDCONTROL_SRC_DIR/$CARDCONTROL_WEBSERVER_SERVICE $CARDCONTROL_SERVICES_DIR
cp $CARDCONTROL_SRC_DIR/$CARDCONTROL_DISPLAYSTATS_SERVICE $CARDCONTROL_SERVICES_DIR

systemctl enable cardcontrol-webservice.service
systemctl enable cardcontrol-display-stats.service

systemctl restart cardcontrol-webservice.service
systemctl restart cardcontrol-display-stats.service