import java.util.*;

public class AStarAlgorithm {

    public static class Node implements Comparable<Node> {
        public final String id;
        public double gCost; // Cost from start to this node
        public double hCost; // Heuristic cost to goal
        public double fCost; // gCost + hCost
        public Node parent;

        public Node(String id) {
            this.id = id;
            this.gCost = Double.POSITIVE_INFINITY;
            this.hCost = 0;
            this.fCost = Double.POSITIVE_INFINITY;
            this.parent = null;
        }

        @Override
        public int compareTo(Node other) {
            return Double.compare(this.fCost, other.fCost);
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Node)) return false;
            Node node = (Node)o;
            return id.equals(node.id);
        }

        @Override
        public int hashCode() {
            return id.hashCode();
        }
    }

    public interface Graph {
        List<Node> getNeighbors(Node node);
        double getCost(Node from, Node to);
        double getHeuristic(Node node, Node goal);
    }

    /**
     * Finds path from start to goal using A* algorithm.
     * @param graph the graph to search on
     * @param start start node
     * @param goal goal node
     * @return List of nodes representing path from start to goal, or empty if none.
     */
    public List<Node> findPath(Graph graph, Node start, Node goal) {
        PriorityQueue<Node> openSet = new PriorityQueue<>();
        HashSet<Node> closedSet = new HashSet<>();

        start.gCost = 0;
        start.hCost = graph.getHeuristic(start, goal);
        start.fCost = start.hCost;
        openSet.add(start);

        while (!openSet.isEmpty()) {
            Node current = openSet.poll();

            if (current.equals(goal)) {
                return reconstructPath(current);
            }

            closedSet.add(current);

            for (Node neighbor : graph.getNeighbors(current)) {
                if (closedSet.contains(neighbor)) {
                    continue;
                }

                double tentative_gCost = current.gCost + graph.getCost(current, neighbor);

                boolean inOpenSet = openSet.contains(neighbor);
                if (!inOpenSet || tentative_gCost < neighbor.gCost) {
                    neighbor.parent = current;
                    neighbor.gCost = tentative_gCost;
                    neighbor.hCost = graph.getHeuristic(neighbor, goal);
                    neighbor.fCost = neighbor.gCost + neighbor.hCost;

                    if (!inOpenSet) {
                        openSet.add(neighbor);
                    } else {
                        // Remove and re-add to update position in PriorityQueue
                        openSet.remove(neighbor);
                        openSet.add(neighbor);
                    }
                }
            }
        }

        return Collections.emptyList(); // No path found
    }

    private List<Node> reconstructPath(Node current) {
        List<Node> path = new ArrayList<>();
        while (current != null) {
            path.add(current);
            current = current.parent;
        }
        Collections.reverse(path);
        return path;
    }
}