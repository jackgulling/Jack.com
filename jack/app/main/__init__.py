# _. - -""""--._
#     .'            '.
#   .'      /\        \
#  /       /  \        \
# |       /====\        |
# |      |= _ _ =|       |
# |      | (o_o) |       |
# |      \  ‾ ‾  /       |
#  \       \____/       /
#   '.                 .'
#     '-._         _.-'
#         """ - ----"""


from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes