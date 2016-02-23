TIMESTAMP=$(date +%m%d%y%H%M%S)

mkdir -p ${CATALINA_HOME}/undeploy/${TIMESTAMP}/
mv ${CATALINA_HOME}/webapps/OMS.war /${CATALINA_HOME}/undeploy/${TIMESTAMP}/OMS.war
sleep 10
sh ${CATALINA_HOME}/bin/shutdown.sh
