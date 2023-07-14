# Inference lambda docker

* **Description:** Lambda that accepts a payload with the characteristics for the model prediction with an id , generates the prediction of a risk model and returns it in a dictionary with the result. 

* **Input:** Features extracted by an id, the accepted format would be a dictionary within a dictionary.

Example:

```json
{
    "5008807" : { 
        "1" : 32, 
        "2" : 12, 
        "3" : 2, 
        "4" : 119, 
        "5" : 45
    }
}
```

* **Output:** A simple dictionary with the value of the prediction as value.
Example:

```json
{
  "risk_prediction": 0
}
```
### Architecture

![Architecture](https://github.com/DataEngel/inference-lambda/assets/63415652/9e71f83c-0b4f-48d4-82d6-87bbbb60245c)
