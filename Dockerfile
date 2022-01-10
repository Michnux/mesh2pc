#http://www.cloudcompare.net/forum/viewtopic.php?t=3552 - - > run cc headless

#FROM tswetnam/xpra-cc:cudagl-18.04

FROM ubuntu:20.04

RUN apt-get -o Acquire::Check-Valid-Until=false -o Acquire::Check-Date=false update
RUN apt-get -y install cloudcompare

#USER root
#RUN apt-get -y install python3.8
RUN apt-get -y install python3-pip
RUN apt-get -y install xvfb

#RUN apt-get update && apt-get install -y software-properties-common gcc && \
#RUN add-apt-repository -y ppa:deadsnakes/ppa

#RUN apt-get update && apt-get install -y python3.8 python3-distutils python3-pip python3-apt

COPY requirements.txt ./
RUN python3 -m pip install --trusted-host=pypi.org --trusted-host=files.pythonhosted.org -r requirements.txt

COPY script_dir /home/script_dir/
#COPY python /home/python/

#CMD ["sleep", "1d"]
CMD ["python3", "/home/script_dir/main.py"]