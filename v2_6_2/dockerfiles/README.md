fab -H 206.189.232.214 --user=trydirect --set=domain=206.189.232.214,installation_id=131,user_token=1  configure_app



When build new image

docker commit -m "" modx optimum/cms:modx-2.6.2-s
docker push optimum/cms:modx-2.6.2-s
docker push registry.try.direct:5000/optimum/cms:modx-2.6.2-s