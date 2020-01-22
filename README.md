# redis-consistency
Show consistency examples using fire and forget, transactions and scripting

### results
After 4 concurrent runs, counts must be equal to 200 or 50 per run

```
# fire and forget [67 missing]
127.0.0.1:6379> get count:ff
"133"

# transaction [consistent]
127.0.0.1:6379> get count:tx
"200"

# scripting [consistent and faster]
get count:sc
"200"
```
