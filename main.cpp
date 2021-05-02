#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Node
{
public:
    int parent;
    int child;
    int weight;
    Node() {}
    Node(int parent, int child, int weight) : parent(parent), child(child), weight(weight) {}
};

int N;
vector<int> tree; //array based tree
int parent, child, weight;
vector<Node> nodes;
int result;

void print_tree()
{
    for (int n = 1; n <= N; n++)
    {
        cout << n << ":" << tree[n] << " ";
    }
    cout << endl;
}

int main()
{
    //io setting
    {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        cout.tie(nullptr);
    }

    //init
    {
        cin >> N;
        tree.resize(N + 1, 0);
        nodes.resize(N);
        for (int n = N - 1; n >= 1; n--)
        {
            cin >> parent >> child >> weight;
            nodes[n] = {parent, child, weight};
        }
    }

    //repeat
    {
        for (Node node : nodes)
        {
            result = max(result, tree[node.parent] + tree[node.child] + node.weight);
            tree[node.parent] = max(tree[node.parent], tree[node.child] + node.weight);
        }
    }

    //output
    {
        cout << result << endl;
    }
    return 0;
}