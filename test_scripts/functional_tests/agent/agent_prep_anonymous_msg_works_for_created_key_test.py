"""
Created on Dec 20, 2017

@author: nhan.nguyen
Verify that user can prepare an anonymous message that associates with a verkey
"""

from indy import agent, signus
import pytest

from test_scripts.functional_tests.agent.agent_test_base import AgentTestBase
from utilities import utils, common


class TestAgentPrepAnonymousMessage(AgentTestBase):

    @pytest.mark.asyncio
    async def test(self):
        # 1. Created wallet.
        # 2. Open wallet.
        self.wallet_handle = await common.create_and_open_wallet_for_steps(
            self.steps, self.wallet_name, self.pool_name)

        # 3. Create "recipient_verkey" with "signus.created_and_store_my_did".
        self.steps.add_step(
            "Create 'recipient_verkey' with 'signus.created_and_store_my_did'")
        (_, self.recipient_verkey) = await utils.perform(
            self.steps, signus.create_and_store_my_did, self.wallet_handle,
            "{}", ignore_exception=False)

        # 4. Prepare anonymous message.
        self.steps.add_step("Prepare anonymous message")
        self.encrypted_msg = await utils.perform(self.steps,
                                                 agent.prep_anonymous_msg,
                                                 self.recipient_verkey,
                                                 self.message,
                                                 ignore_exception=False)

        # 5. Parsed 'encrypted_message'.
        # 6. Check 'parsed_message'
        # 7. Check 'parsed_verkey'
        await super()._parsed_and_check_encrypted_msg()
