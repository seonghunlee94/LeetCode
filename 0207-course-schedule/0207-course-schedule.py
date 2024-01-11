class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)

        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)

        # 순환 구조 확인을 위한 DFS 함수
        def hasCycle(course, traced, visited):
            # 이미 방문한 노드이면 True 반환
            if course in traced:
                return True

            # 이미 확인한 노드이면 False 반환
            if course in visited:
                return False

            # 순환 구조 확인
            traced.add(course)
            for next_course in graph[course]:
                if hasCycle(next_course, traced, visited):
                    return True

            # 탐색 완료 후 순환 구조 확인을 위한 노드를 방문 집합에 추가
            traced.remove(course)
            visited.add(course)

            return False

        # 모든 노드에 대해 순환 구조 확인
        for course in range(numCourses):
            traced = set()
            visited = set()

            # 한 번이라도 순환 구조가 있으면 False 반환
            if hasCycle(course, traced, visited):
                return False

        # 모든 수업을 마칠 수 있으면 True 반환
        return True
        



            
            
        
        
        
        
