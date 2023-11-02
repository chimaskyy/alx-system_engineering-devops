# Networking Basics
## OSI(Open System Interconnection)
A conceptual framework that standardizes and defines the functions of a telecommunication or networking system. It's designed to help understand and organize the various aspects of networking, allowing different technologies and protocols to work together.


## OSI is Made up of 7 layers
### Pysical Layer:
The physical layer deals with the actual physical transmission of data over the network medium. It defines the hardware, cables, connectors, and the physical characteristics of the medium. Example of the pysical layer; cables, Modem, Routers, Switches, Connectors etc.

### Data Link layer:
Responsible for establishing a reliable link between two directly connected nodes and ensuring error detection and correction. It is divided into two sub-layers: Logical Link Control (LLC) and Media Access Control (MAC). Ethernet is an example of a data link layer technology.

### Network Layer:
The network layer focuses on routing data between different networks. It addresses issues such as logical addressing (IP addresses), routing, and packet forwarding. Routers operate at this layer.

### Transport Layer:
The transport layer ensures end-to-end communication and data transfer reliability between systems. It provides error checking, flow control, and data segmentation. TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are examples of transport layer protocols.

### Session Layer:
The session layer is responsible for establishing, maintaining, and terminating sessions between applications. It manages the dialogue between applications, including synchronization and error recovery. NetBIOS and RPC (Remote Procedure Call) are examples of session layer services.

### Presentation Layer:
The presentation layer deals with data format translation, encryption, compression, and other transformations to ensure data is presented in a readable and understandable format. Examples include data encryption and data compression.

### Application Layer:
The application layer provides the interface between the application and the network. It includes application protocols for services such as email (SMTP), web browsing (HTTP), and file transfer (FTP). It is the layer closest to the end user.

The OSI model is organized in a hierarchical manner, where each layer builds on the functionalities provided by the layers below it. Data is encapsulated as it moves down the layers and decapsulated as it moves up the layers. The lower layers handle the physical aspects and fundamental data movement, while the higher layers focus on the application-specific functions.

## LAN
A LAN (Local Area Network) is a network that is confined to a relatively small geographic area, such as a home, office building, school, or campus. LANs are designed to connect devices and computers within this limited area to facilitate data sharing, resource sharing, and communication among users and devices.

### LAN Usage

* LANs are commonly used for local, everyday network needs, such as connecting computers, printers, servers, and other devices to share resources like files, printers, and internet access.
* They provide a platform for local services and applications, including file sharing, local email, online gaming, and communication within a single building or campus.
* LANs are often used for intranets, which are private networks within an organization, and they can be connected to the internet to provide external access.

### Geographical size
* LANs are typically small in terms of geographical size, covering a limited area. The size can vary but is usually within a single building, a floor of a building, or a small campus.
* The physical size of a LAN depends on the specific requirements of the organization, but it's limited to a few kilometers at most.
* LANs can also be small-scale home networks connecting devices within a residence.In a LAN, devices are connected using wired technologies (such as Ethernet) or wireless technologies (such as Wi-Fi). LANs are often set up using a router or switch to manage traffic and provide network connectivity.

## WAN
A WAN (Wide Area Network) is a type of network that spans a large geographical area, connecting multiple LANs (Local Area Networks) and other network segments over a wide area. WANs are designed to facilitate long-distance communication and data exchange between devices, computers, and networks that are physically separated by significant distances.

### LAN Usage
* WANs are commonly used to interconnect LANs and other networks located in different cities, regions, or even countries.
* They provide long-distance connectivity and data transfer, making it possible for organizations to establish communication between remote offices, branches, data centers, and partner networks.

### Geographical Size:
WANs cover a wide geographical area, often spanning regions, countries, or even continents.

## IP Address
An IP (Internet Protocol) address is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication. IP addresses serve two primary functions: network identification and location addressing. They allow devices to find and communicate with each other on the internet.

## Localhost
Localhost" is a hostname that refers to the current device used to access it. It is used to access the network services that are running on the host via the loopback network interface. In simpler terms, when you access "localhost," you are connecting to your own device, typically your own computer. It's often used for testing and development. IP address of 127.0.0.0

## Subnet
A subnet, short for "subnetwork," is a division of an IP network into smaller, more manageable segments. Subnetting helps improve network organization, security, and performance. Subnets are typically used within organizations to separate devices and manage network traffic more effectively. Each subnet has its own range of IP addresses and may be associated with specific departments or functions within an organization.

## IPv4/IPv6
IPv4 uses a 32-bit address format, allowing for approximately 4.3 billion unique IP addresses. As more devices connected to the internet, it became clear that the pool of available IPv4 addresses would soon be depleted. IPv6, with its 128-bit address format, provides a vastly larger address space, allowing for an almost infinite number of unique IP addresses. 

## TCP/UDP
TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are the two main data transfer protocols used at the transport layer (Layer 4) of the OSI model for IP-based communication.

### Difference between TCP and UDP
* TCP is connection-oriented and provides reliable, ordered, and error-checked data delivery. It establishes a connection, ensures data is delivered in the correct order, and retransmits lost or corrupted packets. It's commonly used for applications where data accuracy and order are critical, such as web browsing and file transfer (e.g., HTTP and FTP).
* UDP is connectionless and offers faster but less reliable data transfer. It does not establish a connection, does not guarantee packet order, and does not retransmit lost packets. It's used when speed is more important than guaranteed delivery, as in real-time applications like online gaming and streaming.

## Port
A port is a 16-bit number used to identify specific processes or services running on a device in a network. Ports are associated with IP addresses to enable communication with a specific application or service on that device. Ports can be thought of as virtual doors that allow data to enter and exit specific applications or services. They are used to differentiate between multiple services running on the same device.

## Port numbers
* SSH (Secure Shell): Port 22
* HTTP (Hypertext Transfer Protocol): Port 80
* HTTPS (Hypertext Transfer Protocol Secure): Port 443.

## Tool/Protocol for Checking Device Connectivity
* A commonly used tool/protocol to check if a device is connected to a network is "Ping." The "ping" command sends ICMP (Internet Control Message Protocol) echo requests to a target device or IP address. If the target device is reachable and connected to the network, it responds with ICMP echo replies. Ping is often used to test network connectivity and diagnose network issues, such as determining whether a host is online or estimating network latency.
```
ping <IP_ADDRESS>
```
