# local_run.sh does the following:

# build and run the docker locally with the following features:
#     - host machine work_dir mapped to /home/work_dir in the docker
#     - env variable DELAIRSTACK_PROCESS_WORKDIR set to /home/work_dir/

# please note that simu_work_dir should contain a simulated inputs.json file as it will be set when running the docker on Alteia



# docker build -t pcvs3d .
# docker run -it -v work_dir:/home/work_dir --env DELAIRSTACK_PROCESS_WORKDIR='/home/work_dir/' --name mesh2pc_1 mesh2pc


# docker run -it -v C:\Users\michael.delagarde\Documents\DEV\mesh2pc\work_dir:/home/work_dir -e DELAIRSTACK_PROCESS_WORKDIR='/home/work_dir/' --name mesh2pc_1 mesh2pc
# docker run -it -v C:\Users\michael.delagarde\Documents\DEV\CustomAnalytics\mesh2pc\python:/home/python -e DELAIRSTACK_PROCESS_WORKDIR='/home/work_dir/' --name mesh2pc_1 mesh2pc


# xvfb-run CloudCompare -SILENT \
# -O ./untitled1.obj \
# -SAMPLE_MESH POINTS 500000


#push to docker hub
docker build -t docker.io/michaeldelagarde/mesh2pc .
docker push docker.io/michaeldelagarde/mesh2pc:latest