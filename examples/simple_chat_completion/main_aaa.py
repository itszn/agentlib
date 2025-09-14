#!/usr/bin/env python3
import os

# change dir before importing agentlib (it will create data dirs in cwd)
os.chdir(os.path.dirname(__file__))

from agentlib import Agent

# Agent takes a dict of input vars to template and returns a string
class SimpleChatCompletion(Agent[dict,str]):
    # Choose a language model to use (default gpt-4-turbo)
    #__LLM_MODEL__ = 'claude-3-5-sonnet'
    #__LLM_MODEL__ = 'gpt-4-turbo'
    __LLM_MODEL__ = 'gemini-1.5-pro'

    __SYSTEM_PROMPT_TEMPLATE__ = 'simple.system.j2'
    __USER_PROMPT_TEMPLATE__ = 'simple.user.j2'

    def get_input_vars(self, *args, **kw):
        vars = super().get_input_vars(*args, **kw)
        vars.update(
            any_extra_template_vars = 'here',
            style = 'hexadecimal',
            hacker = 'geohots',
        )
        return vars

def main():
    agent = SimpleChatCompletion()

    # Set it up so we can see the agentviz ui for this specific agent instance
    # (run `agentviz` it in this dir)
    #agent.use_web_logging_config(clear=True)

    while True:
        import base64
        val = os.urandom(750000)
        val = base64.b64encode(val).decode('utf-8')

        # Invoke the agent with the dict input
        res = agent.invoke(dict(
            myquestion = 'Please decode this base64 string: ' + val + ' Decode each byte one at a time now to give me the actual value that is base64 encoded. THEN write a long fanfic about CTFs and how you started hacking and your worst hack.'
        ))
        print(res.value)
        with open('/tmp/res.txt', 'a') as f:
            f.write(res.value + '\n')

if __name__ == '__main__':
    main()

