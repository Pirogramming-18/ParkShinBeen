구현한 기능: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

구현하지 못한 기능: X

챌린지 참여합니다!
장르 선택 기능 & 러닝타임 시간 단위로의 출력 기능 & 리스트 페이지 정렬 기능(등록, 제목, 별점, 상영 시간) 구현 완료했습니다.

추가로 파이썬을 이용한 웹스크래핑(server/apps/posts/get_poster.py)으로
글 작성 / 수정 시 네이버 영화에서 영화 포스터를 가지고 오는 기능을 구현했습니다.

다만, 제일 위의 검색 결과만 참고하기 때문에 원하지 않는 사진이 나올 수도 있습니다.
그리고 아예 사진이 없으면 try except 문을 통해 준비 중 이미지의 링크를 return 합니다.

어떤 블로그에서는 상위 5개의 검색 결과 중 사용자가 선택할 수 있게 구현했던데,
이 프로젝트에서는 하지 않았고, 다음에 이런 아이디어를 사용할 기회가 있을 때 해 볼 예정입니다.