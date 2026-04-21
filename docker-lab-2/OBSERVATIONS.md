## What components do you see running in `kube-system`? Can you identify any components from the lecture (scheduler, etcd, api-server)?
In the kube-system namespace, I saw core Kubernetes components such as kube-apiserver, kube-scheduler, etcd, and kube-controller-manager. These are the main control plane components we learned in the lecture. For example, the API server handles all requests, the scheduler assigns pods to nodes, and etcd stores cluster data.

## In the Events section of `kubectl describe`, what sequence of events happened before the pod started running? Which component scheduled the pod?
Scheduler pod assigned to the one node. And image pulled. Container created. And than Container started.
kube-scheduler is scheduled the pod's component.

## Why does `platform.node()` return the pod name? What does this tell you about container networking isolation?
platform.node() returns the pod name because in Kubernetes each pod gets its own hostname. This shows that each pod runs in an isolated environment with its own network identity. So every pod is separate and has its own network and hostname.

## After deleting the pod manually, did Kubernetes bring it back? Why or why not?
No, Kubernetes did not bring the pod back after deleting it. This is because the pod was created manually and was not managed by any controller. Kubernetes only automatically recreates pods if they are controlled by objects like Deployments or ReplicaSets.

## What would need to be different (hint: think about what you'll learn in Lecture 4) for Kubernetes to automatically restart a deleted pod?
For Kubernetes to automatically restart the pod, it should be created using a Deployment or ReplicaSet. These controllers continuously ensure that the desired number of pods are running, so if one is deleted, a new one is created.

## After deleting the pod manually, did Kubernetes bring it back? Why or why not?
## What would need to be different (hint: think about what you'll learn in Lecture 4) for Kubernetes to automatically restart a deleted pod?

1. What is the difference between running a container with `docker run` and deploying a pod with `kubectl run`? Both used the same image — what changed?
docker run starts a container directly on the local machine. kubectl run creates a pod in the Kubernetes cluster. Even though both use the same image, Kubernetes adds features like scheduling, networking, and management, so the container runs inside a managed environment.

2. In `kubectl describe pod`, what is the role of the **Scheduler** event? Which control plane component does that correspond to?
The Scheduler event shows that the pod has been assigned to a specific node. This corresponds to the kube-scheduler component in the control plane, which decides where the pod should run.

3. In `kubectl get pods -n kube-system`, name two components you recognised from the lecture and describe what they do.
kube-scheduler: Decides which node a pod should run on.
etcd: Stores all cluster data such as configurations and current state.

4. **Image-specific observation** (answer only the one relevant to your image):
   - 🐘 Postgres: Why did the pod crash in Task 4 without environment variables? What does this tell you about how images communicate their requirements?
   The Postgres pod crashed because required environment variables (like POSTGRES_PASSWORD) were not provided. This shows that some Docker images depend on environment variables to work properly. These variables define required configurations for the container.

5. Task 6 reflection: After deleting the pod, Kubernetes did **not** restart it. In one paragraph, explain why, and what Kubernetes object would change this behaviour.
After deleting the pod, Kubernetes did not restart it because the pod was not managed by any higher-level controller. It was just a standalone pod, so once deleted, it was gone permanently. If the pod had been created using a Deployment or ReplicaSet, Kubernetes would automatically recreate it to maintain the desired state.