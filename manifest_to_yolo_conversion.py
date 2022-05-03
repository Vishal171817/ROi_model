import json
import argparse

def convert_manifest_to_yolo(filename,yolo_directory,manifest_job_name):
  with open(filename) as fp:
    Lines = fp.readLines()
    for line in Lines:
      dict1 = {}
      dict1.update(json.loads(line.strip()))
      if(len(dict1['source-ref'])>0):
        source_id= dict1['source-ref']
        x=source_id.split("/")[3].split(".")[0]+'.txt'
        name= yolo_directory+x
        if (len(dict1[manifest_job_name]['annotations'])>0):
          print(name)
          with open(name,'w') as filehandle:
            for x1 in range(len(dict1[manifest_job_name]['annotations'])):
              object_id = dict1[manifest_job_name]['annotations'][x1]['class_id']
              x = dict1[manifest_job_name]['annotations'][x1]['left']/dict1[manifest_job_name]['image_size'][0]['width']
              y = dict1[manifest_job_name]['annotations'][x1]['top']/dict1[manifest_job_name]['image_size'][0]['height']
              width = dict1[manifest_job_name]['annotations'][x1]['width']/dict1[manifest_job_name]['image_size'][0]['width']
              height = dict1[manifest_job_name]['annotations'][x1]['height']/dict1[manifest_job_name]['image_size'][0]['height']
              object_id = int(object_id)
              L = [str(object_id)," ",str(x)," ",str(y)," ",str(width)," ",str(height)]
              filehandle.writelines(L)
              filehandle.writelines('\n')
              
              
              
              
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--manifest-job-name',type=str)
  parser.add_argument('--filename',type=str)
  parser.add_argument('--output-dir',type=str)
  args, _ = parser.parse_known_args()
  convert_manifest_to_yolo(args.filename,args.output_dir,args.manifest_job_name)
  
            

