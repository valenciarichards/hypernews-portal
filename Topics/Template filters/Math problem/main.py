template = """
<html>
  <div> a + b + c = {{ sum | default:0 | add:a | add:b | add:c }} </div>
</html>
"""
