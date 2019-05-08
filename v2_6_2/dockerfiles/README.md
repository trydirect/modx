When build new image

docker commit -m "" modx optimum/cms:modx-2.6.2-s
docker push optimum/cms:modx-2.6.2-s
docker push registry.try.direct:5000/optimum/cms:modx-2.6.2-s
