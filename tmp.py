import re



bad_attrs = ['width', 'height', 'style', '[-a-z]*color', 'background[-a-z]*', 'on*']
single_quoted = "'[^']+'"
double_quoted = '"[^"]+"'
non_space = '[^ "\'>]+'
h = re.compile("<" # open
    "([^>]+) " # prefix
    "(?:%s) *" % ('|'.join(bad_attrs),) + # undesirable attributes
    '= *(?:%s|%s|%s)' % (non_space, single_quoted, double_quoted) + # value
    "([^>]*)"  # postfix
    ">"        # end
, re.I)


if __name__ == "__main__":
    html = "<xiaojie   xiaojie  width='aaa'  >"
    r = h.sub("acv",html)
    print(r)
    p = re.compile("\d")
    print(p.sub("d","aaa3aaa4aaa543aaa4"))
