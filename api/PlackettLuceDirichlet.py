from flask_restful import Resource, reqparse
from models import plackett_luce_dirichlet
from api.arguments.default_arguments import add_default_arguments
from api.arguments.dirichlet_arguments import add_dirichlet_arguments
from api.transforms.default_transforms import (
    poc_share_transform,
    poc_support_for_poc_candidates_transform,
    poc_support_for_white_candidates_transform,
    white_support_for_white_candidates_transform,
    white_support_for_poc_candidates_transform,
    num_ballots_transform,
    seats_open_transform,
    num_white_candidates_transform,
    num_poc_candidates_transform,
    num_simulations_transform,
)
from api.transforms.dirichlet_transforms import concentration_transform

# Arguments for the plackettLuceDirichlet resource
parser = reqparse.RequestParser()
add_default_arguments(parser)
add_dirichlet_arguments(parser)


class PlackettLuceDirichlet(Resource):
    def get(self):
        args = parser.parse_args()
        poc_elected_rcv, _ = plackett_luce_dirichlet(
            poc_share=poc_share_transform(args),
            poc_support_for_poc_candidates=poc_support_for_poc_candidates_transform(args),
            poc_support_for_white_candidates=poc_support_for_white_candidates_transform(args),
            white_support_for_white_candidates=white_support_for_white_candidates_transform(args),
            white_support_for_poc_candidates=white_support_for_poc_candidates_transform(args),
            num_ballots=num_ballots_transform(args),
            seats_open=seats_open_transform(args),
            num_white_candidates=num_poc_candidates_transform(args),
            num_poc_candidates=num_white_candidates_transform(args),
            concentrations=concentration_transform(args),
            num_simulations=num_simulations_transform(args),
        )
        return dict({'poc_elected_rcv': poc_elected_rcv, 'seats_open': seats_open_transform(args)})
