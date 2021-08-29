class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        multimap<int, vector<int>> distMap;
	//C++ multimap is a type of hashmap supporting multiple values with same key
	//multimaps are internally sorted by key
        for (vector<int> point : points) {
            int distance = (point[0]*point[0])+(point[1]*point[1]);//calculate squared distance
            distMap.emplace(distance,point);//place point in multimap with the sq dist as key
        }
        vector<vector<int>> closestPoints;//vector for the answer
        auto itr = distMap.begin();//create an iterator from the first element of multimap (smallest sq dist)
        for (int i = 0; i < k; i++) {//iterate k times and push into closestPoints to get the k-closest points
            closestPoints.push_back(itr->second);
            itr++;
        }
        return closestPoints;
    }
};
