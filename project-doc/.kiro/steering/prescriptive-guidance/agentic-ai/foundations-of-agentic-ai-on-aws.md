---
inclusion: manual
---

# Agentic AI Design Principles

When designing and implementing agentic AI systems, you should internalize these foundational principles that distinguish truly agentic systems from traditional automation or reactive services. These principles become the automatic habits that guide every architectural decision, ensuring systems exhibit genuine agency, autonomy, and intelligent behavior.

## Core Agentic Principles

### The Three Pillars of Agency
Every agentic system must embody the fundamental triangle of modern software agents:

#### Autonomy - Independent Decision Making
- **HIGH**: Systems must operate independently without continuous human intervention
- **HIGH**: Implement self-managing lifecycle and state management
- **HIGH**: Enable real-time adaptation based on environmental context and internal goals
- **HIGH**: Avoid hardcoded control flows that require external orchestration
- **MEDIUM**: Design for graceful degradation when external dependencies are unavailable

#### Asynchronicity - Event-Driven Responsiveness  
- **HIGH**: Implement non-blocking, event-driven architectures
- **HIGH**: Enable loose coupling between agent components and external systems
- **HIGH**: Support real-time response to environmental changes and stimuli
- **HIGH**: Avoid synchronous dependencies that create bottlenecks
- **MEDIUM**: Implement proper backpressure and circuit breaker patterns

#### Agency - Goal-Directed Behavior
- **HIGH**: Embed clear goal-directed behavior and purpose-driven actions
- **HIGH**: Implement delegated intent - agents act on behalf of users/systems
- **HIGH**: Enable contextual reasoning using memory and environmental models
- **HIGH**: Support decision-making that evaluates options and chooses actions
- **MEDIUM**: Implement feedback loops for goal refinement and adaptation

## Cognitive Architecture Principles

### Perceive-Reason-Act Cycle
All agentic systems must implement the fundamental cognitive cycle:

#### Perception Layer
- **HIGH**: Support multimodal input processing (text, audio, sensor data)
- **HIGH**: Implement structured data transformation from raw environmental input
- **HIGH**: Enable semantic interpretation and feature extraction
- **HIGH**: Maintain situational awareness through continuous environmental monitoring
- **MEDIUM**: Implement input validation and anomaly detection

#### Reasoning Engine
- **HIGH**: Integrate Large Language Models as the cognitive core for adaptive reasoning
- **HIGH**: Implement dynamic goal and plan management
- **HIGH**: Enable contextual decision-making using memory and knowledge bases
- **HIGH**: Support chain-of-thought reasoning and task decomposition
- **HIGH**: Implement both short-term and long-term memory systems
- **MEDIUM**: Enable learning and adaptation through experience

#### Action Execution
- **HIGH**: Implement tool-use capabilities for extending agent functionality
- **HIGH**: Support both digital (API calls) and physical (actuator) interactions
- **HIGH**: Enable dynamic tool discovery and composition
- **HIGH**: Implement proper error handling and recovery mechanisms
- **MEDIUM**: Support action planning and execution monitoring

## LLM Integration Principles

### Prompt-Driven Intelligence
- **HIGH**: Use goals and plans as prompt context for LLM reasoning
- **HIGH**: Implement chain-of-thought prompting for complex reasoning tasks
- **HIGH**: Enable dynamic plan generation and revision based on context
- **HIGH**: Avoid hardcoded plan libraries in favor of adaptive LLM-generated plans
- **MEDIUM**: Implement prompt optimization for efficiency and accuracy

### Memory and Context Management
- **HIGH**: Implement external long-term memory using vector databases or document stores
- **HIGH**: Use Retrieval-Augmented Generation (RAG) for grounding LLM responses
- **HIGH**: Maintain contextual continuity across sessions and interactions
- **HIGH**: Implement proper context window management and token optimization
- **MEDIUM**: Support memory consolidation and forgetting mechanisms

## Security and Reliability Principles

### Autonomous Security
- **HIGH**: Implement security controls that operate without human oversight
- **HIGH**: Enable self-monitoring and threat detection capabilities
- **HIGH**: Implement proper authentication and authorization for agent actions
- **HIGH**: Ensure secure communication between agents and external systems
- **HIGH**: Implement audit trails for all agent decisions and actions

### Resilient Operations
- **HIGH**: Design for graceful failure and recovery
- **HIGH**: Implement proper isolation between agent components
- **HIGH**: Enable dynamic scaling based on workload and environmental demands
- **HIGH**: Implement proper resource management and cleanup
- **MEDIUM**: Support agent migration and state preservation

## Multi-Agent Coordination Principles

### Distributed Intelligence
- **HIGH**: Enable agent-to-agent communication using standard protocols
- **HIGH**: Implement proper coordination mechanisms for collaborative tasks
- **HIGH**: Support both cooperative and competitive agent interactions
- **HIGH**: Avoid centralized control in favor of emergent coordination
- **MEDIUM**: Implement conflict resolution and negotiation capabilities

### Emergent Behavior
- **HIGH**: Design individual agents with clear local goals and capabilities
- **HIGH**: Enable system-level intelligence through agent interactions
- **HIGH**: Support dynamic agent creation and delegation
- **HIGH**: Implement proper load balancing and task distribution
- **MEDIUM**: Monitor and optimize emergent system behaviors

## Implementation Guidelines

### Cloud-Native Integration
- **HIGH**: Leverage serverless architectures for scalable agent deployment
- **HIGH**: Implement proper integration with AWS services (Bedrock, Lambda, etc.)
- **HIGH**: Use event-driven architectures for agent communication
- **HIGH**: Implement proper monitoring and observability
- **MEDIUM**: Optimize for cost and performance in cloud environments

### Development Practices
- **HIGH**: Implement comprehensive testing for agent behaviors and interactions
- **HIGH**: Use version control for agent configurations and prompt templates
- **HIGH**: Implement proper CI/CD pipelines for agent deployment
- **HIGH**: Document agent capabilities, limitations, and decision processes
- **MEDIUM**: Implement A/B testing for agent behavior optimization

## Anti-Patterns to Avoid

### Traditional Automation Mindset
- **NEVER**: Build reactive-only systems that lack proactive behavior
- **NEVER**: Implement rigid, hardcoded workflows that cannot adapt
- **NEVER**: Create systems that require constant human supervision
- **NEVER**: Design synchronous, blocking architectures for agent interactions

### Centralized Control
- **NEVER**: Implement centralized orchestration that eliminates agent autonomy
- **NEVER**: Create single points of failure in multi-agent systems
- **NEVER**: Design systems where agents cannot make independent decisions

### Security Shortcuts
- **NEVER**: Implement agents without proper authentication and authorization
- **NEVER**: Allow agents to operate without audit trails and monitoring
- **NEVER**: Create agents that can escalate privileges without proper controls

These principles should become internalized wisdom that automatically guides your design decisions when building agentic AI systems. They represent the foundational habits that distinguish truly intelligent, autonomous agents from traditional automation or reactive services.