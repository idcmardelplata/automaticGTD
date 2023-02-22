import unittest
from sample.inbox import inboxmodule as inbox

def test_should_allow_user_to_add_new_input():
    assert inbox.addNewInput("content")


class TestInbox(unittest.TestCase):
    def test_should_only_allow_user_to_add_new_input_if_has_content(self) -> None:
        self.assertFalse(inbox.addNewInput(""))



if __name__ == "__main__":
    unittest.main()
