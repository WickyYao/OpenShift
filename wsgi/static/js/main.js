create_room_comet = function(ts) {
  if (ts == null) {
    ts = '';
  }
  return $.getJSON("/comet?ts=" + ts, function(result) {
      if (result.data){
        room_content(result.data);
      }
      return create_room_comet(result.ts);
  });
};

room_content = function(data) {
  contents = data.content;
  html = ''
  for (i = 0; i < contents.length; i++) {
    content = contents[i];
    html += "<tr>"+
              "<td>"+contents[i].content+"</td>"+
              "<td>"+contents[i].created+"</td>"+
              "</tr>"
  }
  $('#chat_content table').append(html)
  $("#chat_content table tr:last-child").get(0).scrollIntoView()
  return;
};
