1. What is the difference between a Pod and a Deployment? Why would you use a Deployment instead of a bare Pod?
The pod is the smallest unit in Kubernetes. It runs the container. If bare pod crashes, it stays dead and nothing will restarts it automatically. Controller Manager always keeps watching. If pod went down, it will create the new one. That's why we use Deployments instead of bare Pods in practice.

2. Why is a ConfigMap used for the MongoDB URL instead of hardcoding it in the Deployment YAML?
Instead of hardcoding the MongoDB URL directly in the deployment YAML, we used configMap. That means, if the server name changes, we only need to update the configMap in one place instead of editing every YAML file.

3. What happened to the original Pod when you scaled the WebApp to 3 replicas? Did it get replaced, or were new Pods added alongside it?
When i change the replicas from 1 to 3 and ran kubectl apply, the original pos was not replaced. Two new pods were added alongsize it. The oriğginal pod had just been created. The controller manager noticed that 3 replicas were required but only 1 existed, so it created  the missing 2 automatically.

4. What would happen to the application if the MongoDB Pod crashed? How would Kubernetes respond?
Kubernetes will create the new one. The webapp would reconnect the mongo-service, fo the connection itself would cover. If all data stored in MongoDB would be lost when the pod restarts. 

5. What is one thing that surprised you or that you found confusing? How did you resolve it?
The task instructions mentioned mongodb-configmap.yaml but the actual files in the cloned repo were named differently (mongo-config.yaml, mongo-secret.yaml). I resolved it by running ls to list the files and used the correct names. I also got an error with kubectl version --short since that flag was removed in newer versions of kubectl — I fixed it by simply running kubectl version instead. This issue was because of the version of kubectl.