# SOLID and SOLID-RL data

  - **Self-seeding data.** The self-seeding data is available in self-seef directory: [data/self-seeds](./self-seeds).

  - **SFT data.** SOLID data to be sued for Supervised Fine-tuning (SFT) data for training SOLID-RL:

    1. SFT data, without length-based mixed quality training: [Download](https://www.dropbox.com/scl/fi/ix78lhl7qsvlf275fpliz/data_SFT-WoDPO-WoMixQ.json?rlkey=9m669pe9oj3jv8uc7obeby280&dl=0)
    2. SFT data, with length-based mixed quality training: [Download](https://www.dropbox.com/scl/fi/nhop5ilg6lo0vkz5qg1t1/data_SOLID-SFT-WoDPO-MixQV2.json?rlkey=l6qxklfyfys16gfda8qcaf9v3&dl=0)

  - **DPO data.** We provide SOLID data to be used as `chosen` inspired by original DPO work and also to be used `rejected` inspired by self-play. Please note that based on our experiments:

    1. With length-based mixed quality training (SOLID used as `chosen` and SFT used as `rejected`: [Download](https://www.dropbox.com/scl/fi/i817cf0b1xks1c4bcvht6/DPO_data_SOLID-SFT-WoDPO-MixQV2.json-SOLIDChosen-SFTRejected.json?rlkey=k8dlqclf0vae3wg17g66uvfk1&dl=0)
    2. With length-based mixed quality training (SOLID used as `rejected` and SFT used as `chosen`: [Download](https://www.dropbox.com/scl/fi/1fdpe1kmym45epqjjuiud/DPO_data_SOLID-SFT-WoDPO-MixQV2.json-SOLIDRejected-SFTChosen.json?rlkey=7laxv1er7u4iq4vv2q3o5p247&dl=0)


