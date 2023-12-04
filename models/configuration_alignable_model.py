from collections import OrderedDict, namedtuple
from typing import Any, List, Mapping, Optional 

from transformers import PreTrainedTokenizer, TensorType, is_torch_available
from transformers.configuration_utils import PretrainedConfig

from models.interventions import VanillaIntervention


AlignableRepresentationConfig = namedtuple(
    "AlignableRepresentationConfig", 
    "alignable_layer alignable_representation_type "\
    "alignable_unit max_number_of_units alignable_low_rank_dimension subspace_partition group_key",
    defaults=(0, "block_output", "pos", 1, None, None, None)
)


class AlignableConfig(PretrainedConfig):
    def __init__(
        self,
        alignable_model_type="gpt2",
        alignable_representations=[
            # we do distributed search over elements in the sublist.
            AlignableRepresentationConfig()
        ],
        alignable_interventions_type=VanillaIntervention,
        mode="parallel",
        **kwargs
    ):
        self.alignable_model_type = alignable_model_type
        self.alignable_representations = alignable_representations
        self.alignable_interventions_type = alignable_interventions_type
        self.mode = mode
        super().__init__(**kwargs)
        
