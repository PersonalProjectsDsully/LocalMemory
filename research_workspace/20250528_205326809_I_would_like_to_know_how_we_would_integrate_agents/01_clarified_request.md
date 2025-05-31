# Clarified Research Request

Original Request: I would like to know how we would integrate agents with our FreshService instance for our MSP team where we use Freshservice across our clients. I am looking for recommending solutions to customers, I if it is a query that is out of the agents ability, it should triage it to a human agent. It should also do all of the initial classification of the ticket. This will be running on a single computer with QWEN3 30b with about 32k of context, we can use any python libraries, we will be hosting the qwen model in LM studio and will make requests to it using the rest API. 

Clarifications:
- What are the primary ticket categories/typical queries your MSP team handles across clients?: We typically receive tickets related to IT. This can be for device troubleshooting, software troubleshooting, network outages at different sites, resetting passwords, those types of things. 
- How should the system determine when a query requires human intervention (e.g., specific keywords, complexity levels)?: I think it should do this based on if it is not confident in the answer it is going to give to the user. 
- Do you have existing FreshService automation rules or APIs that need integration with the AI agent?: We do not.
- What level of customization is required for different client environments (e.g., unique ticket types, SLAs)?: We only really need to change the instance url and the api key.
