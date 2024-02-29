import tkinter
from question import OrderedFillInTheBlank, MultipleChoice, TrueOrFalse

quiz_window = tkinter.Tk()
quiz_window.title("AWS Solutions Architect Exam")
quiz_window.minsize(width=500, height=300)
current_question_index = 0

questions = [MultipleChoice(quiz_window, "Which EC2 instance type lets you pay for what you use with no commitment?", ["spot", "on demand", "reserved","dedicated"], 1),
MultipleChoice(quiz_window, "Which type of IP address is a fixed public IP address for your EC2 instance?", ["public", "elastic", "private", "dynamic"], 1),
MultipleChoice(quiz_window, "What is used to defined an EC2 placement strategy?", ['iam group', 'vpc subnet', 'ec2 clusters', 'placement group'], 3),
MultipleChoice(quiz_window, "Which placement strategy clusters instances into low latency group in a single AZ?", ['clusters','high availability','spread','partition'], 0),
MultipleChoice(quiz_window, "Which placement strategy spreads instances across underlying hardware?", ['clusters','high availability','spread','partition'], 2),
MultipleChoice(quiz_window, "Which placement strategy spreads many instances across different racks?", ['clusters','high availability','spread','partition'], 3),
MultipleChoice(quiz_window, "Which placement strategy has the lowest latencdy?", ['clusters','high availability','spread','partition'], 0),
MultipleChoice(quiz_window, "What is the maximum number of instances possible in a spread placement group?", ['6','7','8','9'], 1),
MultipleChoice(quiz_window, "The term used for the logical component in a VPC that represents a virtual network card", ['Elastic network card','Virtual Network Card','Network Card','Elastic Network Interfaces'], 3),
TrueOrFalse(quiz_window, "You can move an ENI an attach them on the fly to other instances", "TRUE"),
TrueOrFalse(quiz_window, "An ENI can be used in any Availablility Zone", "FALSE"),
MultipleChoice(quiz_window, "What is the EC2 feature that saves the RAM state on shutdown?", ['Hibernate','EBS','Instance Store','EC2 recovery'], 0),
TrueOrFalse(quiz_window, "EBS volume persists after an EC2 instance is terminated", "TRUE"),
TrueOrFalse(quiz_window, "Only one EBS volume can be attached to an EC2 instance", "FALSE"),
TrueOrFalse(quiz_window, "EBS volumes are tied to a particular AZ", "TRUE"),
TrueOrFalse(quiz_window, "By default, an EBS root volume is deleted on instance termination", "TRUE"),
TrueOrFalse(quiz_window, "By default, EBS volumes other than the root are not deleted on termination", "TRUE"),
MultipleChoice(quiz_window, "What is used to back an EBS volume?", ['ECS Instance Store','s3 backup','mirroring','EBS Snapshots'], 3),
MultipleChoice(quiz_window, "What is it called when en EBS snapshot is moved to an archive tier?", ['EBS backup','EBS restore','EBS Snapshot Archive','EBS redundancy'], 2),
MultipleChoice(quiz_window, "What can you use to retain an accidentally deleted snapshot?", ['S3 glacier','EBS Recycle Bin','RDS','EBS restore'], 1),
MultipleChoice(quiz_window, "What is used to a full initialization of an EBS snapshot so ther is no latency on first use?", ['EBS Snapshot Archive','Fast Snapshot Restore','S3','EBS backup restore'], 1),
TrueOrFalse(quiz_window, "An AMI is a customization of an EC2 instance", "TRUE"),
MultipleChoice(quiz_window, "Which has better I/O performance?", ['EBS volume','EC2 instance store'], 1),
TrueOrFalse(quiz_window, "Data on an EC2 instance store will survive if the instance is terminated", 'FALSE'),
MultipleChoice(quiz_window, "Which EBS volume is a general purpose SSD that balances price and performance for a variety of workloads?", ['gp2/gp3','io1/io2 block express','st 1','sc 1'], 0),
MultipleChoice(quiz_window, "Which EBS volume is a high performance SSD for critical, low latency workloads?", ['gp2/gp3','io1/io2 block express','st 1','sc 1'], 1),
MultipleChoice(quiz_window, "Which EBS volume is a low cost HDD for frquently accessed, high throughput workloads?", ['gp2/gp3','io1/io2 block express','st 1','sc 1'], 2),
MultipleChoice(quiz_window, "Which EBS volume is the lowest cost HDD volume for less frequest work loads?", ['gp2/gp3','io1/io2 block express','st 1','sc 1'], 3),
MultipleChoice(quiz_window, "Which EBS volume supports attaching to multiple instances?", ['gp2/gp3','io1/io2 block express','st 1','sc 1'], 1),
MultipleChoice(quiz_window, "What is the max amount of instaces an EBS block can attach to?", ['6','3','12','16'], 3),
MultipleChoice(quiz_window, "What is the AWS service that creates a managed network file system for EC2?", ['Amazon S3','Amazon NFS','Amazon EFS','Amazon ECR'], 2),
TrueOrFalse(quiz_window, "EFS works in multilple AZs", "TRUE"),
TrueOrFalse(quiz_window, "EFS only works with linux AMIs", 'TRUE'),
MultipleChoice(quiz_window, "Which load balancer works at layer 7 and supports HTTP/2 and websocket?", ['Network load balancer','application load balancer','classic load balancer','elastic load balancer'],1),
TrueOrFalse(quiz_window, "An application load balancer is not able to route traffic based on the url of a resource", "FALSE"),
MultipleChoice(quiz_window, "Which load balancer works by using forwarding UDP and TCP data?", ['Network load balancer','application load balancer','classic load balancer','elastic load balancer'],0),
TrueOrFalse(quiz_window, "A network load balancer can have more than one static IP per AZ", "false"),
MultipleChoice(quiz_window, "Which load balancer is used for a very high level performance?", ['Network load balancer','application load balancer','classic load balancer','elastic load balancer'],0),
MultipleChoice(quiz_window, "Which load balancer is used to route traffice through firewalls, Itrusion detection systems, etc?", ['Network load balancer','application load balancer','gateway load balancer','elastic load balancer'],2),
TrueOrFalse(quiz_window, "The gateway load balancer uses the GENEVE protocol on port 6081", "TRUE"),
MultipleChoice(quiz_window, "Which load balancer is uses a load balancer and a tranparent network gateway", ['Network load balancer','application load balancer','gateway load balancer','elastic load balancer'],2),
MultipleChoice(quiz_window, "What is it called when a client is always redirected to the same instance behind a load balancer?", ['elastic sessions','Sticky sessions','Cached sessions','ssh sessions'], 1),
MultipleChoice(quiz_window, "What allows traffic to be evenly distributed to host across AZs?", ['network load balancer','Sticky sessions','application load balancing','cross region load balancing'], 3),
MultipleChoice(quiz_window, "What allows you to load multiple SSL certificates on a server?", ['SSL','SNI','SNP','TLS'], 1),
MultipleChoice(quiz_window, 'SNI requires the client to indicate the hostname of target server in the handshake?', "TRUE"),
TrueOrFalse(quiz_window, 'RDS has an auto scaling feature so you do not run out of sspace', "TRUE"),
MultipleChoice(quiz_window, 'What is the purpose of RDS read replicas?', ['Increase read efficiency','security','storage increase','security'], 0),
TrueOrFalse(quiz_window, "RDS read replicas cannot cross AZs", "FALSE"),
TrueOrFalse(quiz_window, "It is free to send data to a read replica in another AZ", "TRUE"),
TrueOrFalse(quiz_window, "You can set up a RDS Multi AZ read replica for disaster recovery.", "TRUE"),
TrueOrFalse(quiz_window, "There will be down time to convert a RDS read replica from single to multi-AZ", "FALSE"),


]


welcome_label = tkinter.Label(quiz_window, text="Welcome to the AWS Solutions Architect Quiz")
welcome_label.pack()

def check_question():
    global current_question_index

    if not questions[current_question_index].question_displayed and current_question_index < len(questions):
        current_question_index += 1
        questions[current_question_index].display_question()

    quiz_window.after(1, check_question)

def display_question():

    welcome_button.destroy()
    welcome_label.destroy()
    
    questions[current_question_index].display_question()
    quiz_window.after(1, check_question)


welcome_button = tkinter.Button(quiz_window, text="Start Quiz", command=display_question)
welcome_button.pack()

quiz_window.mainloop()
