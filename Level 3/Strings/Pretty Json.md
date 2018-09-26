# Pretty Json

Asked in: **Microsoft, Facebook**

Pretty print a json object using proper indentation.

- Every inner brace should increase one indentation to the following lines.
- Every close brace should decrease one indentation to the same line and the following lines.
- The indents can be increased with an additional ‘\t’

**Example 1:**

```
Input : {A:"B",C:{D:"E",F:{G:"H",I:"J"}}}
Output :
{
    A:"B",
    C:
    {
        D:"E",
        F:
        {
            G:"H",
            I:"J"
        }
    }
}
```

**Example 2**

```
Input : ["foo", {"bar":["baz",null,1.0,2]}]
Output :
[
    "foo",
    {
        "bar":
        [
            "baz",
            null,
            1.0,
            2
        ]
    }
]
```

`[]` and `{}` are only acceptable braces in this case.

Assume for this problem that space characters can be done away with.

Your solution should return a list of strings, where each entry corresponds to a single line. The strings should not have “\n” character in them.

## Solution Approach

This is more of a parsing problem.

Make sure you take a lot of time thinking about the corner cases and structure of the code before you start coding.

Fixing corner cases on the fly can make your code really ugly.

Note the following:

1. ‘{‘, ‘[’ have the same effect on the printing

2. ‘}’, ‘]’ have the same effect as well

3. ‘:’ and ‘,’ are the only other 2 characters that matter.

Think about the behavior when you encounter the following characters.

Also think about the behavior based on the following character.

### Where I got stuck

Consider a case
`[{a:b},{c:d}]`

My output was:

```
[
    {
        a:b
    }
    ,
    {
        c:d
    }
]
```

## Code

```python
class Solution:
	# @param A : string
	# @return a list of strings
	def prettyJSON(self, A):
	    res = []
	    t = 0
	    w = ''
        for i in A:
            tabs = ('\t')*t
            # handle {, [
            if i == '{' or i == '[':
                if len(w) > 0:
                    res.append(tabs + w)
                t += 1
                res.append(tabs + i)
                w = ''
            # handle ,
            elif i == ',':
                if len(w) > 0:
                    res.append(tabs + w + ',')
                    w = ''
                else:
                    res[-1] += ','
            # handle }, ]
            elif i == '}' or i == ']':
                if len(w) > 0:
                    res.append(tabs + w)
                t -= 1
                res.append(('\t')*t + i)
                w = ''
            else:
                w += i
        return res
```
