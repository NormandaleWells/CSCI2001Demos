In this lab, we will write tests for a simple module of list-related utilities (list_utils.py).

In class, we'll write tests for `find()` and `count()`.  You will need to write tests for `min_element()` and `max_element()`. These tests should be in classes called `TestMinElement()` and `TestMaxElement()` which test `min_element()` and `max_element()` respectively.

For `min_element()` and `max_element()` your tests should include at least the following:

- Check to make sure they properly return `None` for an empty list.
- Check to make they each work with a 1-element list.
- Test with a list whose first element is the minimum or maximum.
- Test with a list whose last element is the minimum or maximum.
- Test with a list whose elements are all negative.
- Test `min_element()` with a 4-element list whose smallest element is 2**1000.
- Test `max_element()` with a 4-element list whose largest element is -2**1000.

All your tests may use lists of integers.  If you'd like to include a few tests that work with strings or some other data type, feel free to do so.

You should be able to make do with just the `assertEqual()` and `assertIsNone()` methods in the testing framework.  However, if you find a need for any of the others I mentioned in class, feel free to do so.

Note that because we haven't talked about exception in this class, there are a few error conditions I'm not asking you to check:

- You don't need to check lists containing mixed types of elements.
- You don't need to check lists some of whose entries are the value `None`.

This lab will be worth 50 points, but only 10 of these points will result from your code passing the 2 tests in the lab.  The rest will be determined by analysis of your code to make sure you covered all the cases outlined above.