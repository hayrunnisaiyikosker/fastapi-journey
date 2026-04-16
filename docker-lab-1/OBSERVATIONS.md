# Docker Lab 1 — Observations
**Image:** postgres:16-alpine  
**Student:** HAYRUNNİSA İYİKÖŞKER
**Student ID:** 2203060011

## 1. What is the size of your image? Is it large or small — and why do you think that is?
The size of my image is 395 MB. I think this is medium sized and postreSQL system so small. So PostgreSQL is a full relational database engine with many compiled binaries and libraries, which makes the total size larger than a simple Alpine image.

## 2. How many layers does your image have? What does each major layer add?
My image has 24 layers. The most important ones are:
- ADD alpine-minirootfs (9.11MB): adds the Alpine Linux base operating system
- RUN apk add (2.09MB): installs runtime dependencies
- RUN wget postgresql (273MB): downloads and compiles the PostgreSQL source, this is by far the largest layer
- RUN install directories (20.5kB, 12.3kB): creates necessary folders
- COPY docker-entrypoint.sh (36.9kB): adds the startup scripts
- CMD, EXPOSE, ENV layers: these are 0 bytes, they only store metadata

## 3. What operating system and architecture does your image use?
I just saw from docker inspect: 
- Os: linux
- Architecture: amd64
Which means the image runs on 64-bits Linux system using x86_64 processor architecture.

## 4. **Postgres-Image-specific question:**
After I stopped and removed my container with docker stop and docker container rm, I started a brand new container with the same settings When I ran;
SELECT * FROM students, I got this error:
"ERROR: relation students does not exist"
My data gone because Docker containers store their data in a temporary layer. When you remove the container that means the layer is deleted along with everything inside it, include the data base files stores at /var/lib/postresql/data. To make data container restarts and removals, i would need to add a Docker volume to the run command: -v pgdata:/var/lib/postgresql/data This would store the database files on the host machine instead of inside the container.

## 5. In one paragraph: what surprised you most about this lab?
It was the extent to which a container is completely isolated and temporal. I hadn’t realised that my data would be completely gone once I removed the container. When I ran the SELECT query in the new container and received an error message stating that the table did not exist, everything I had done had been deleted. This made it much clearer to me just how temporary the container was. Furthermore, the fact that the largest layer in my image was 273 MB just for downloading and compiling PostgreSQL also indicates just how much preparation was done before the container even started.
