class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

def split_data(X, y, feature, threshold):
    left_indices = [i for i in range(len(X)) if X[i][feature] <= threshold]
    right_indices = [i for i in range(len(X)) if X[i][feature] > threshold]
    return [X[i] for i in left_indices], [X[i] for i in right_indices], [y[i] for i in left_indices], [y[i] for i in right_indices]

def best_split(X, y):
    best_feature, best_threshold, best_gain = None, None, -1
    for feature in range(len(X[0])):
        thresholds = set(x[feature] for x in X)
        for threshold in thresholds:
            left_X, right_X, left_y, right_y = split_data(X, y, feature, threshold)
            if not left_y or not right_y: continue
            gain = len(left_y) / len(y) * (len(left_y) / len(y)) - len(right_y) / len(y) * (len(right_y) / len(y))
            if gain > best_gain:
                best_gain, best_feature, best_threshold = gain, feature, threshold
    return best_feature, best_threshold

def build_tree(X, y):
    if len(set(y)) == 1: return Node(value=y[0])
    feature, threshold = best_split(X, y)
    if feature is None: return Node(value=max(set(y), key=y.count))
    left_X, right_X, left_y, right_y = split_data(X, y, feature, threshold)
    left_node = build_tree(left_X, left_y)
    right_node = build_tree(right_X, right_y)
    return Node(feature, threshold, left_node, right_node)

def predict(tree, x):
    if tree.value is not None: return tree.value
    if x[tree.feature] <= tree.threshold:
        return predict(tree.left, x)
    else:
        return predict(tree.right, x)

X = [[0, 0], [1, 1], [1, 0], [0, 1]]
y = [0, 1, 1, 0]
tree = build_tree(X, y)

# Testing the tree
for x in X:
    print(f"Input: {x}, Predicted: {predict(tree, x)}")
